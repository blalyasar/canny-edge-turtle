cmake_minimum_required(VERSION 3.17)
project(opencv-cpp)
set(CMAKE_CXX_STANDARD 20)
find_package( OpenCV REQUIRED )


include_directories( ${OpenCV_INCLUDE_DIRS} )

# tum isimler aynı  olacak calıstırma dosyasıda aynı

add_executable(opencv-cpp img-canny-point.cpp )


target_link_libraries( opencv-cpp ${OpenCV_LIBS} )
