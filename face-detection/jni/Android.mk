LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

#OPENCV_INSTALL_MODULES:=off
#OPENCV_LIB_TYPE:=SHARED
ifdef OPENCV_ANDROID_SDK
  ifneq ("","$(wildcard $(OPENCV_ANDROID_SDK)/OpenCV.mk)")
    include ${OPENCV_ANDROID_SDK}/OpenCV.mk
  else
    include ${OPENCV_ANDROID_SDK}/sdk/native/jni/OpenCV.mk
  endif
else
  include ../../sdk/native/jni/OpenCV.mk
endif

#LOCAL_SRC_FILES  := DetectionBasedTracker_jni.cpp jni.c image_processor.cpp
#LOCAL_C_INCLUDES += $(LOCAL_PATH)
#LOCAL_LDLIBS     += -llog2 -ldl
#LOCAL_CPPFLAGS  += -O3 -std=c++11

LOCAL_MODULE     := detection_based_tracker

include $(BUILD_SHARED_LIBRARY)

