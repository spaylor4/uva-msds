# TensorFlow Data

Reading: *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* [Ch. 13](https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ch13.html)

- TensorFlow Datasets allow you to gradually read data from disk, which is needed when data is larger than available RAM.
- Datasets contain slices of data and can be iterated over to get each tensor.
- Many available transformations can be applied to Datasets, and these operations can be chained.
  - `.repeat(n)` repeats the data n times.
  - `.batch(n)` breaks the data into batches of tensors of size n.
    - `drop_remainder = True` can be set if you don't want a smaller batch at the end if there aren't enough items available for a full batch.
  - `.map` applies a specified function transformation to each item.
  - `.apply` applies a function to the Dataset as a whole.
  - `.filter` filters items according to a specified criteria function (usually a lambda function).
  - `.take(n)` takes the first n items.
  - `.shuffle(buffer_size, seed)` can be used to shuffle data, to make SGD work better. It loads items from memory into a buffer (up to the buffer size), then randomly returns an item from the buffer when requested and replaces it with the next item from the source data.
    - Important to make buffer size large enough, but without exceeding memory.
    - `repeat` on a shuffled dataset produces a different order for each repeat, unless `reshuffle_each_iteration = False`.
  - For very large data, can be useful to split it into multiple files, then randomly select and interleave to better shuffle. `.list_files(filepaths)` creates a dataset that shuffles the supplied file paths.
    - Best to interleave files of equal length, otherwise no interleaving will occur at end of longest file.
    - Can specify `num_parallel_calls` to read files in parallel. Setting to `tf.data.experimental.AUTOTUNE` tells TensorFlow to automatically choose the right number of threads.
  - `.prefetch(1)` tells the CPU to go ahead and prepare the next batch while the GPU is using a batch for training.
    - Especially when using `num_parallel_calls` in `interleave` and `map` preprocessing  transformations, this can help make the GPU close to 100% utilized.
    - The *memory bandwidth* of a GPU card specifies the number of GBs it can get into or out of the GPUs RAM per second.
    - If a dataset fits in memory, using `cache` after loading/preprocessing (and before shuffling/repeating/batching/prefetching) will speed up performance.
- Keras models can be trained and evaluated using Datasets directly.
- TFRecord is TensorFlow's binary format for storing large amounts of data and reading it efficiently.
  - `tf.data.TFRecordDataset(filepaths_list)` creates a Dataset from a TFRecord file.
    - Can use `num_parallel_reads` to interleave multiple files.
  - `tf.data.TFRecordWriter('filepath.tfrecord')` creates a TFRecord file.
    - Can use `tf.io.TFRecordOptions(compression_type="GZIP")` to compress file.
- TFRecord files usually contain *protobufs* (serialized protocol buffers) that contain the schema definition.
  - An Example protobuf represents one instance of a dataset.
  - Features can be BytesList, FloatList, or Int64List.
  - A BytesList can contain any binary data, such as jpegs using `tf.io.encode_jpeg()` to convert to binary.
- Preprocessing for neural nets requires converting all input features to numeric and generally normalizing them.
  - Categorical features can be converted to numeric with one-hot encoding (for 10 or fewer categories) or embeddings (for 50+ categories).
    - Can create an embedding layer with `keras.layers.Embedding`.

### Video: Data API, TFRecord, and TFDS

- Models do better with more training data - tradeoff between data collection and algorithm development.
- Deep learning models often trained with huge datasets that won't fit in RAM: makes preprocessing/normaling, truly randomly selecting minibatches, using typical hardware, and assuming data is all numeric very difficult.
- Tensor: container for numerical data (multidimensional array). Scalar is 0D, vector 1D, matrix 2D, and higher dimensions.
  - Images are 4D tensors: examples, height, width, channels (such as RGB).
- Batch dimension/axis is the first axis considered in a batch tensor.
- TensorFlow Data API revolves around concept of a dataset (sequence of data items).
  - Can iterate over a dataset to access each tensor.
  - Can chain transformations (e.g. `.repeat`, `.batch`, `.filter`, and `.map`) together.
- Shuffling a dataset helps ensure that minibatches are iid (SGD works best when this holds).
  - Interleaving mixes records from different files (useful when data too big to store in memory). `.interleave` reads files in parallel threads.
- Prefetching tries to stay one batch ahead (working in parallel) to reduce waiting time on GPUs doing optimization.
- TFRecord is a format for storing large amounts of data efficiently in binary format.
  - CSV is inefficient and doesn't support complex data structures (like video/audio) very well.
  - Use `tf.io.TFRecordWriter` to create these files.
  - Protobuf: serialized protocol buffer, a portable & extensible binary format.
  - Similar to json.
  - To parse examples, use a description dictionary.
- TensorFlow Datasets (TFDS) Project: Google project providing datasets for download.
  - `import tensorflow_datasets as tfds`

### Video: Encoding Categorical and Textual Features

- Neural nets do not take raw text as input, so words must be converted to numeric vectors. Three ways of doing so:
  - Segment into words and transform each word into a vector.
  - Segment into characters and transform each char into a vector.
  - Extract n-grams (consecutive words) and transform each into a vector.
- When you have a small number of categories in a categorical feature, you can use one-hot encoding.
  - First encode categories in a lookup table (using index). Use out-of-vocabulary buckets to assign unknown categories.
  - Then use `tf.one_hot()` to convert lookup index into one-hot vector.
    - `depth` parameter is equal to length of vocab (number of categories) plus number of out-of-vocab buckets.
  - `keras.layers.TextVectorization` performs the above steps for you.
  - One-hot encoding doesn't work as well for large vocabularies since each vector is very large. Also, order of categories has no intrinsic meaning.
- Word embedding embeds each category into a vectorized feature space.
  - E.g. man, woman, king, queen can have gender, royalty, and age features. In this way, similar words are similar in this embedded space (man and king will be close together, apple and orange will be close, apple and man will not) when the mapping to embedded space is good.
    - Likewise, synonyms should be embedded into similar vectors, reflecting the *semantic relationship*.
  - t-SNE (t-distributed stochastic neighbor embedding) can project high dimensions down to 2 for visualization.
  - Can use vector arithmetic to map from one category to another (king - man + woman $\approx$ queen).
  - Word embeddings are dense (one-hot encodings are sparse), lower-dimensional, and learned from data (one-hot are hard coded).
  - Word embeddings can be pre-trained or learned jointly with the main task using `keras.layers.Embedding`. 
    - Lots of good pre-trained embeddings available, most famously Word2vec, or GloVe.
  - Rule of thumb: embeddings should have between 16 and 512 dimensions, depending on task and vocab size.
  - Word embeddings sometimes capture biases (e.g. man : doctor :: woman : nurse) gathered from human-written text used for training.
    - Word neutralization is an important research topic - Bolukbasi paper. Can project to neutral axis words that shouldn't be gendered, and equalize gender-appropriate pairs.

### Class Notes

*March 8, 2021*

- Difference between tf Tensor and Dataset: Dataset is a generator - has ability to loop through without immediately storing anything. Iterating through gives an individual tensor each time.
  - "Small memory footprint"
  - Tensors are tf's version of an immutable matrix.

- Need to have bit-32 for tf, not 64 (both float and int).
- `dataset.batch(n)` divides dataset into batches of length $n$, where each batch is a tensor.
  - `dataset.unbatch()` takes all elements in a dataset and puts them in their own tensor.
- `dataset.shuffle(buffer_size=n)` shuffles data in an iterative fashion (to make good use of memory).
  - Buffer size is a window within which each element is sampled. So buffer size of two randomly chooses first element from first two in dataset, then chooses next from third element along with the unselected element from first two, and so on.
  - There is a command line utility `gshuf` for shuffling data files in bash, before even getting to tf.
- If you have enough RAM, might not want to re-preprocess at each epoch - can use `.cache()` method in tf.