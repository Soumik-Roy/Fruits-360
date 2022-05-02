import tensorflow as tf

saved_dir = "saved_models/cnn_model2"

converter = tf.lite.TFLiteConverter.from_saved_model(saved_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
model_lite = converter.convert()


with open("cnn_model.tflite", 'wb') as f:
    f.write(model_lite)

# f = open("labels.txt", "w")
# for i in range(131):
#     f.write(str(i)+'\n')
# f.close()