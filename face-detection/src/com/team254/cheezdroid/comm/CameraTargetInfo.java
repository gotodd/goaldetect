package com.team254.cheezdroid.comm;

import android.util.Log;

import org.json.JSONException;
import org.json.JSONObject;

public class CameraTargetInfo {
    protected double m_y;
    protected double m_z;
    protected double m_w; //width
    protected double m_h; //height

    // Coordinate frame:
    // +x is out the camera's optical axis
    // +y is to the left of the image
    // +z is to the top of the image
    // We assume the x component of all targets is +1.0 (since this is homogeneous)
    public CameraTargetInfo(double y, double z, double w, double h) {
        m_y = y;
        m_z = z;
        m_w = w;
        m_h = h;
    }

    private double doubleize(double value) {
        double leftover = value % 1;
        if (leftover < 1e-7) {
            value += 1e-7;
        }
        return value;
    }

    public double getY() {
        return m_y;
    }

    public double getZ() {
        return m_z;
    }
    public double getW() {
        return m_w;
    }
    public double getH() {
        return m_h;
    }

    public JSONObject toJson() {
        JSONObject j = new JSONObject();
        try {
            j.put("y", doubleize(getY()));
            j.put("z", doubleize(getZ()));
            j.put("w", doubleize(getW()));
            j.put("h", doubleize(getH()));
        } catch (JSONException e) {
            Log.e("CameraTargetInfo", "Could not encode Json");
        }
        return j;
    }
}
