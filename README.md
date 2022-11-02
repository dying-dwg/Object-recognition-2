# Object recognition and determination of the parameters of their spatial rotation and scaling by the correlation method in the polar-logarithmic coordinate system

Conversion  the resulting images from standard graphic format files into two-dimensional arrays of pixels suitable for computer processing (using Intel OpenCV)
Center the main image, scale it with a coefficient K= 1+0.05×2 and rotate by φ = (+3×2)° relative to its central pixel, also leave the dimensions of the original image. For centering, zooming and rotating the image, I used the affine matrix acquisition function (see getRotationMatrix2D) and the affine transformation function (cv.warpAffine).
Next, I conversion the main and modified into a polar-logarithmic coordinate system. To do this, I will use the function to conversion the image from one CS to another (LogPolar), then flip the image 90 degrees (rot90) and get the main and modified images in polar-logarithmic CS.
Last stage is using the template matching function (matchTemplate) to find the correlation field between the main and the modified image.

### Example of work
> Main and modified image

<img src="https://user-images.githubusercontent.com/66872084/199547033-0ff68a96-07dc-4707-8672-5b33989b8dc6.jpg" width="400"> <img src="https://user-images.githubusercontent.com/66872084/199547077-3eb6a776-cc17-483c-9d08-c6162e379a50.jpg" width="400">

> Main and modified image (polar-logarithmic CS)

<img src="https://user-images.githubusercontent.com/66872084/199549324-280efe5d-8b3b-4f39-a11c-af7d066b50fa.jpg" width="400"> <img src="https://user-images.githubusercontent.com/66872084/199549333-5c22da8e-07a7-4022-baf5-f5ce60b39368.jpg" width="400">

> Correlation field
<img src="https://user-images.githubusercontent.com/66872084/199550113-af52d347-eb47-4eab-95df-a289fd2fd46d.jpg" width="400">

### Using libraries
- cv2 - OpenCV used to read image (imread), rotate (getRotationMatrix2D + warpAffine), conversion to the polar-logarithmic coordinate system (logPolar), getting a correlation field (Template Matching), save image (imwrite)
- time - To count the working hours
- numpy - For working with arrays
- matplotlib (pyplot) - To create and output graphs
- os - To get a list of files in a directory.
____

# Распознавание объектов на изображении и определение параметров их пространственного вращения и масштабирования методом корреляции в полярно-логарифмической системе координат

Перевести полученные изображения, из файлов стандартного графического формата в двумерные массивы пикселов, пригодные для компьютерной обработки (используя Intel OpenCV)
Центрировать исходное изображение, масштабировать его с коэффициентом K= 1+0.05×2 и повернуть на φ = (+3×2)° относительно его центрального пиксела, также оставить размеры исходного изображения. Для центрирования, изменения масштаба и поворота изображения воспользовался функцией получения аффинной матрицы (см.getRotationMatrix2D) и функцией аффинного преобразования (cv.warpAffine).
Далее перевожу основное и изменённое в полярно-логарифмическую систему координат. Для этого воспользуюсь функцией для перевода изображения из одной ск в другую (logPolar), далее переворачиваю изображение на 90 градусов (rot90) и получаю исходное и изменённое изображения в полярно-логарифмической ск.
И последний этап - использую функцию сопоставления шаблонов (matchTemplate), чтобы найти корреляционное поле между основным и изменённым изображением.
