# rgb2gray2brightness
사진의 밝기를 계산하는 함수 코드입니다.\
사진 파일의 경로를 함수 파라미터로 넘겨주면 해당 파일의 밝기를 %단위로 반환합니다. (값이 클 수록 밝은 사진)

opencv를 이용하여 코드를 작성하면 매우 쉽지만\
개인적으로 프로젝트를 진행하면서 opencv를 설치하기 어려운 경우가 있었고\
opencv 없이 사진의 밝기를 구하는 방법을 많이 검색해보았지만 정리된 코드가 없는 것 같아\
opencv를 사용하지 않고 python에서 기본적으로 제공해주는 라이브러리들만 이용하여 코드를 작성해보았습니다.

---

It is a function code that calculates the brightness of the image file.\
If you hand over the path of an image file to a function parameter, it returns the brightness of the image file in units of %. (The bigger the value, the brighter the image.)

It's very easy to write a code using opencv,\
but somtimes, there were times when it was difficult and complicated to install opencv while working on a project.\
I searched a lot for how to get brightness of image without using opencv, but I don't think there's an organized code.\
Therefore, I wrote the code using only the libraries provided by Python by default without using opencv.
