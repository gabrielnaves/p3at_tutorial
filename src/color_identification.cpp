#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <sensor_msgs/image_encodings.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>

#include <cstdio>
#include <string>

const std::string image_topic = "/camera/image_raw";
const std::string raw_image_window_name = "raw image";
const std::string thresh_image_window_name = "thresholded image";

cv::Mat raw_image;
std::string found_color;
int low_h, low_s, low_v, high_h, high_s, high_v;

void receiveFrame(const sensor_msgs::ImageConstPtr& msg);
bool isImageValid(const cv::Mat& img);
void findColor();

int main(int argc, char **argv) {
    ros::init(argc, argv, "color_identification_node");
    ros::NodeHandle node_handle;
    image_transport::ImageTransport img_transport(node_handle);
    image_transport::Subscriber frame_sub = img_transport.subscribe(image_topic.c_str(), 1, receiveFrame);
    cv::namedWindow(raw_image_window_name);
    cv::namedWindow(thresh_image_window_name);

    while(ros::ok()) {
        if (isImageValid(raw_image))
            findColor();
        ros::spinOnce();
        cv::waitKey(30);
    }
    return 0;
}

void receiveFrame(const sensor_msgs::ImageConstPtr& msg)
{
    cv_bridge::CvImagePtr cv_ptr;
    try {
        cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
    }
    catch (cv_bridge::Exception &e) {
        ROS_ERROR("cv_bridge exception: %s", e.what());
        return;
    }
    cv_ptr->image.copyTo(raw_image);
}

bool isImageValid(const cv::Mat& img) {
    return not (img.rows == 0 or img.cols == 0);
}

void findColor() {
    cv::Mat hsv;
    cv::cvtColor(raw_image, hsv, cv::COLOR_BGR2HSV);
    cv::Mat thresh;
	cv::inRange(hsv, Scalar(low_h,low_s,low_v), Scalar(high_h,high_s,high_v), thresh);
    cv::imshow(raw_image_window_name, raw_image);
    cv::imshow(thresh_image_window_name, thresh);
}
