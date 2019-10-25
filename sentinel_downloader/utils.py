import cv2


def save_image(image_array, path):
    """
    save numpy array image to specific path
    :param image_array: Numpy array
    :param path: Path to save
    :return:
    """
    cv2.imwrite(path, image_array)


def show_image(image_array=None, path=None, mode=cv2.IMREAD_COLOR):
    """
    Show image from numpy array or path
    :param image_array: numpy array
    :param path: path to image
    :param mode: cv2.IMREAD_COLOR: It specifies to load a color image.
                 Any transparency of image will be neglected. It is the default flag.
                 Alternatively, we can pass integer value 1 for this flag.
                 cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode.
                 Alternatively, we can pass integer value 0 for this flag.
                 cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel
                 Alternatively, we can pass integer value -1 for this flag.
    :return: None
    """

    if image_array and path:
        Exception("Cannot provide both parameters image_array and path")

    if image_array:
        cv2.imshow("image", image_array)

    if path:
        image_array = cv2.imread("watch.jpg", mode)
        cv2.imshow("image", image_array)


def load_image(path, mode=cv2.IMREAD_COLOR):
    """

    :param path: Path to image
    :param mode: cv2.IMREAD_COLOR: It specifies to load a color image.
                 Any transparency of image will be neglected. It is the default flag.
                 Alternatively, we can pass integer value 1 for this flag.
                 cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode.
                 Alternatively, we can pass integer value 0 for this flag.
                 cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel
                 Alternatively, we can pass integer value -1 for this flag.
    :return: Numpy array
    """
    return cv2.imread("watch.jpg", mode)
