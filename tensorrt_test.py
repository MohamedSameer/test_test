import tensorrt as trt

# Create a logger
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

# Create a TensorRT engine builder
builder = trt.Builder(TRT_LOGGER)
print("TensorRT builder created successfully.")
