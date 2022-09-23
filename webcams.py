# test script for

import cv2

def list_cameras():



    """
    Test the ports and returns a tuple with the available ports and the ones that are working.
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    while len(non_working_ports) < 6:  # if there are more than 5 non working ports stop the testing.
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
            print("Port %s is not working." % dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" % (dev_port, h, w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." % (dev_port, h, w))
                available_ports.append(dev_port)
        dev_port += 1
    return available_ports, working_ports, non_working_ports




def main():

    available_ports, working_ports, non_working_ports = list_cameras()

    print('ports are {}, working ports {}, non working ports {}'.format(str(available_ports), (working_ports), (non_working_ports)))

    video_capture_0 = cv2.VideoCapture(0)
    video_capture_1 = cv2.VideoCapture(1)
    video_capture_2 = cv2.VideoCapture(2)
    video_capture_3 = cv2.VideoCapture(3)


    while True:
        # Capture frame-by-frame
        ret0, frame0 = video_capture_0.read()
        ret1, frame1 = video_capture_1.read()
        ret2, frame2 = video_capture_2.read()
        ret3, frame3 = video_capture_3.read()

        if ret0:
            # Display the resulting frame
            cv2.imshow('Cam 0', frame0)

        if ret1:
            # Display the resulting frame
            cv2.imshow('Cam 1', frame1)

        if ret2:
            cv2.imshow('Cam 2', frame2)

        if ret3:
            cv2.imshow('Cam 3', frame3)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture_0.release()
    video_capture_1.release()
    video_capture_2.release()
    video_capture_3.release()


    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
