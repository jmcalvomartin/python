# -*- coding: utf-8 -*-
"""
WallyAI

@author: Jorge Calvo
"""

from matplotlib import pyplot as plt
import os
import numpy as np
import sys
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from flask_socketio import SocketIO
from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone


try:
    from PIL import Image
except ImportError:
    import Image
    
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
Bootstrap(app)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'static'),
    # Flask-Dropzone config:
    DROPZONE_DEFAULT_MESSAGE="Arrastra o Click para añadir tu tablero de Wally",
    DROPZONE_ALLOWED_FILE_CUSTOM=True,
    DROPZONE_ALLOWED_FILE_TYPE='.jpg, .jpeg, .png',
    DROPZONE_INVALID_FILE_TYPE="Solo puedes subir imagenes",
    DROPZONE_MAX_FILE_EXCEED="solo se puede subir un tablero de Wally",
    DROPZONE_UPLOAD_MULTIPLE=False,
    DROPZONE_BROWSER_UNSUPPORTED="Tu navegador no soporta el arrastre de archivos",
    DROPZONE_MAX_FILE_SIZE=8,
    DROPZONE_MAX_FILES=1,
    DROPZONE_IN_FORM=True,
    DROPZONE_UPLOAD_ON_CLICK=True,
    DROPZONE_UPLOAD_ACTION='upload',  
    DROPZONE_UPLOAD_BTN_ID='submit',
)

dropzone = Dropzone(app)
socketio = SocketIO(app)

@app.route('/',methods=['POST', 'GET'])
def index():
     return render_template('index.html')
 
@app.route('/send', methods=['POST'])
def upload():
    global ext
    for key, f in request.files.items():
        if key.startswith('file'):
            namefile=f.filename
            ext = namefile.split('.')[1];
            f.save(os.path.join(app.config['UPLOADED_PATH'], "wally_ia."+ ext))
    return '', 204

@app.route('/wally',methods=['POST', 'GET'])
def wally():
            

    return render_template("ia.html")


@app.route('/ia',methods=['POST', 'GET'])
def ia():

    model_path = './trained_model/frozen_inference_graph.pb'
    
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(model_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    
    def load_image_into_numpy_array(image):
      (im_width, im_height) = image.size
      return np.array(image.getdata()).reshape(
          (im_height, im_width, 3)).astype(np.uint8)
    
    label_map = label_map_util.load_labelmap('./trained_model/labels.txt')
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    with detection_graph.as_default():
      with tf.Session(graph=detection_graph) as sess:
        image_np = load_image_into_numpy_array(Image.open('./static/wally_ia.' + ext))
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        scores = detection_graph.get_tensor_by_name('detection_scores:0')
        classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')
        # Actual detection.
        (boxes, scores, classes, num_detections) = sess.run(
            [boxes, scores, classes, num_detections],
            feed_dict={image_tensor: np.expand_dims(image_np, axis=0)})
    
        if scores[0][0] < 0.1:
            sys.exit('No está Wally')
        

        print('Wally encontrado')
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=6)
        plt.figure(figsize=(15, 11))
        plt.imshow(image_np)
        plt.savefig('./static/wally_found.' + ext)
    return render_template("results.html")
   
    

if __name__ == '__main__':
    socketio.run(app)
    
    