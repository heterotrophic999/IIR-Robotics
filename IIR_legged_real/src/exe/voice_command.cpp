#include <ros/ros.h>
#include <unitree_legged_msgs/HighCmd.h>
#include <unitree_legged_msgs/HighState.h>
#include "unitree_legged_sdk/unitree_legged_sdk.h"
#include "convert.h"
#include <std_msgs/UInt8.h>

// UNITREE_LEGGED_REAL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

using namespace UNITREE_LEGGED_SDK;

int flag = 0;
void AlisaCallback(const std_msgs::UInt8 msg) {
    int move = msg.data;
    if (move == 1)
        flag = 1;
    else if (move == 2)
        flag = 2;
    else if (move == 3)
        flag = 3;
    else if (move == 4)
        flag = 4;
    else if (move == 5)
        flag = 5;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "dance");

    std::cout << "WARNING: Control level is set to HIGH-level." << std::endl
        << "Make sure the robot is standing on the ground." << std::endl
        << "Press Enter to continue..." << std::endl;
    std::cin.ignore();

    ros::NodeHandle nh;

    ros::Rate loop_rate(500); // 500hz

    long motiontime = 0;

    unitree_legged_msgs::HighCmd high_cmd_ros;

    ros::Publisher pub = nh.advertise<unitree_legged_msgs::HighCmd>("high_cmd", 1000);
    ros::Subscriber sub = nh.subscribe("alice", 1000, AlisaCallback);

    while (ros::ok())
    {

        motiontime += 2; // time in microseconds

        high_cmd_ros.head[0] = 0xFE;
        high_cmd_ros.head[1] = 0xEF;
        high_cmd_ros.levelFlag = HIGHLEVEL;
        high_cmd_ros.mode = 0;
        high_cmd_ros.gaitType = 0;
        high_cmd_ros.speedLevel = 0;
        high_cmd_ros.footRaiseHeight = 0;
        high_cmd_ros.bodyHeight = 0;
        high_cmd_ros.euler[0] = 0;
        high_cmd_ros.euler[1] = 0;
        high_cmd_ros.euler[2] = 0;
        high_cmd_ros.velocity[0] = 0.0f;
        high_cmd_ros.velocity[1] = 0.0f;
        high_cmd_ros.yawSpeed = 0.0f;
        high_cmd_ros.reserve = 0;

        if (flag == 4) {
            high_cmd_ros.mode = 12; // dance 1
            pub.publish(high_cmd_ros);
            usleep(2000000); // waiting 2s
            flag = 0;
            high_cmd_ros.mode = 0;
            pub.publish(high_cmd_ros);
            //high_cmd_ros.mode = 6; // position adjustment
            //pub.publish(high_cmd_ros);
            //usleep(1000000); // waiting 1s
        }
        else if (flag == 1) {
            high_cmd_ros.mode = 0; // stand
            pub.publish(high_cmd_ros);
            usleep(2000000); // waiting 2s
            flag = 0;
            //high_cmd_ros.mode = 6; // position adjustment
            //pub.publish(high_cmd_ros);
            //usleep(1000000); // waiting 1s
        }
        else if (flag == 2) {
            high_cmd_ros.mode = 10; // 90 degree rotation with a jump.
            pub.publish(high_cmd_ros);
            usleep(2000000); // waiting 2s
            flag = 0;
            high_cmd_ros.mode = 0;
            pub.publish(high_cmd_ros);
            //high_cmd_ros.mode = 6; // position adjustment
            //pub.publish(high_cmd_ros);
            //usleep(1000000); // waiting 1s
        }
        else if (flag == 3) {
            high_cmd_ros.mode = 11; // asks
            pub.publish(high_cmd_ros);
            usleep(4000000); // waiting 4s
            flag = 0;
            high_cmd_ros.mode = 0;
            pub.publish(high_cmd_ros);
            //high_cmd_ros.mode = 6; // position adjustment
            //pub.publish(high_cmd_ros);
            //usleep(1000000); // waiting 1s
        }
        else if (flag == 5) {
            high_cmd_ros.mode = 13; // dance 2
            pub.publish(high_cmd_ros);
            usleep(2000000); // waiting 2s
            flag = 0;
            high_cmd_ros.mode = 0;
            pub.publish(high_cmd_ros);
            //high_cmd_ros.mode = 6; // position adjustment
            //pub.publish(high_cmd_ros);
            //usleep(1000000); // waiting 1s
        }


        ros::spinOnce();
        loop_rate.sleep(); // 2 ms delay
    }

    return 0;
}
