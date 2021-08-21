#include <opencv2/highgui.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main() {
    string path = samples::findFile("../ortak-veri/enemy-logo-tek.png"); 
    //string path = samples::findFile("whatsapppp.jpg"); 
    
    Mat img = imread(path, IMREAD_COLOR);
    resize(img,img,Size(img.cols/4,img.rows/4),INTER_CUBIC);

    Mat detectedEdges,idx;
    Canny(img, detectedEdges, 50, 100);
    findNonZero(detectedEdges, idx);
    FileStorage fs("idxprofil.xml", FileStorage::WRITE);
    fs << "cannyresult" << idx;
    imshow("Detected Edges", detectedEdges);
    waitKey(0);
    ////read example
    
    
    FileStorage xmlR;
    xmlR.open("idx.xml", FileStorage::READ);
    
    Mat B;
    
    xmlR["cannyresult"] >> B;
    
    std::cout << B << std::endl;
    
    xmlR.release();
    imshow("Detected Edges xml", B);

    // Mat dst;
    // cv::normalize(B, dst, 0, 1, cv::NORM_MINMAX);
    // imshow("test", dst);

    // drawKeypoints(dst, B, dst)


   // waitKey(0);
    return 0;
}
