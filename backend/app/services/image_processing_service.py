import cv2
from matplotlib import image
import numpy as np


class ImageProcessingService:

    @staticmethod
    def load_image(path: str):

        return cv2.imread(path)
    @staticmethod
    
    def grayscale(image):

        return cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    @staticmethod
    def denoise(image):import cv2


class ImageProcessingService:
    """
    Image preprocessing service used before OCR.
    """

    @staticmethod
    def load_image(path: str):

        image = cv2.imread(path)

        if image is None:
            raise FileNotFoundError(
                f"Unable to load image: {path}"
            )

        return image

    @staticmethod
    def grayscale(image):

        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

    @staticmethod
    def resize(
        image,
        scale: float = 2.0
    ):

        return cv2.resize(
            image,
            None,
            fx=scale,
            fy=scale,
            interpolation=cv2.INTER_CUBIC
        )

    @staticmethod
    def denoise(image):

        return cv2.medianBlur(
            image,
            3
        )

    @staticmethod
    def threshold(image):

        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            10
        )

    @staticmethod
    def morphology(image):

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (2, 2)
        )

        image = cv2.morphologyEx(
            image,
            cv2.MORPH_OPEN,
            kernel
        )

        image = cv2.morphologyEx(
            image,
            cv2.MORPH_CLOSE,
            kernel
        )

        return image

    @classmethod
    def preprocess(
        cls,
        path: str
    ):

        image = cls.load_image(path)

        image = cls.grayscale(image)

        image = cls.resize(image)

        image = cls.denoise(image)

        image = cls.threshold(image)

        image = cls.morphology(image)

        return image

        return cv2.medianBlur(
        image,
        3
    )
        
    @staticmethod
    def denoise(image):

        return cv2.medianBlur(
        image,
        3
    )
        
    @classmethod
    def preprocess(cls, path):

        image = cls.load_image(path)

        image = cls.grayscale(image)

        image = cls.denoise(image)

        image = cls.threshold(image)

        return image