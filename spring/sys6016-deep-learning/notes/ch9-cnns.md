# CNNs



### Video: Convolutions and Pooling Layers

- CNNs inspired by the human visual cortex architecture.
  - Some neurons have a larger receptive field and react to more complex patterns based on the output of lower-level neurons with smaller local receptive fields.
  - LeCun created the first CNN to recognize handwritten numbers.
- CNNs are built from convolutional layers and pooling layers.
- Convolution operation takes an input (array of data) and a kernel (array of parameters).
  - Kernel is placed on top of the image and the dot product (sum of element/pixel-wise product) is computed. Then the kernel is moved left to right, then up to down (one pixel at a time) and the product is computed again at each step.
  - Output is also a 2D image.
- Convolution leverages three properties that improve ML systems:
  - Sparse interactions: since the kernel is smaller than the input image, every output unit doesn't interact with every input unit. This leads to improved statistical efficiency from having fewer parameters and less memory.
    - O(k x n) vs O(m x n), where k is several orders of magnitude smaller than m.
    - Each neuron in the second layer is connected only to first layer neurons in its receptive field.
  - Parameter sharing: the kernel parameters are used at every position of the input (unlike traditional networks in which each element of the weight matrix is used exactly once when computing the output layer).
  - Equivariance representation: convolution is equivariant to translation. This means that if its input changes, its output changes in the same way.
    - For a function $g(I)$, convolution($g(I)$) = $g(\text{conv}(I))$. This means that convolution creates a feature map of where certain patterns appear in an image.
- Can detect many image features by stacking multiple feature maps.
  - CNNs follow a spatial hierarchy: first layer learns local patterns, then next layer learns larger patterns based on features from first layer, and so on.
- CNN hyperparameters:
  - Same/zero padding: convolution operation shrinks the image unless it is padded with zeros around the edge.
  - Stride: increasing the stride makes the image shrink faster by moving by more pixels at one time.
    - Skips some input locations. Equivalent to downsampling after the convolution.
- Pooling layers aim to subsample the original image to reduce computational load, memory usage, and number of params. Each neuron in a pooling layer is connected to the outputs of a limited number of neurons in the previous layer (in a receptive field).
  - Pooling neurons have no weights, and just take the max or average of the inputs.
  - Max pooling introduces invariance: input can change dramatically and only cause small change in output. It is "invariant to small translation" in the inputs.
- Can implement in keras with Sequential model and `keras.layers.Conv2D` and `keras.layers.maxPooling2D` layers.
  - Can have multiple combinations of convolutional and pooling layers, and will eventually need a `keras.layers.flatten` and some dense layers and an activation layer.

### Video: Successful CNN Architectures

- CNNs are everywhere these days: self-driving cars, art transfer, etc.
- Typical CNN architectures stack a few convolutional layers (each followed by a ReLU layer), then a pooling layer, then more convolutional layers and another pooling layer and so on. Then, after these layers have gotten deeper/smaller, there is a regular feedforward network of fully connected layers (and a ReLU) followed by a softmax output layer.
- LeNet-5 was first CNN. AlexNet improved on it using larger and deeper network than LeNet-5, stacking convolutional layers directly on top of each other, and using ReLU instead of tanh.
- GoogLeNet was the next big improvement: 10x fewer params than AlexNet, but much deeper than previous CNNs. Introduced inception (network within a network).
  - Naive inception applies parallel operations on the input from the previous layer and concatenates all filter outputs together depth wise (which means output will be thick - expensive to compute).
    - To prevent feature depth from growing at every layer, use a 1x1 convolution to get a single pixel (flat) surface. Can then control thickness by number of 1x1 convolutional filters. This projects depth to lower dimensions by combining feature maps.
  - No fully connected layers except output layer.

- ResNet is an extremely deep (152 layer network) that took 2-3 weeks to train with 8 GPUs.
  - Although this is very deep, he found that deeper is not necessarily better (showed that a 20-layer network performed better than 56-layer).
    - Deeper networks are harder to optimize.
  - Deeper network should perform at least as well as shallower if skip connections are used.
    - Forces network to learn residuals.
    - Skipping avoids problems from dead neurons close to zero.