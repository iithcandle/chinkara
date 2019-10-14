# By CSI camera:

```
cs18resch01001@nano-ub18:~$ rostopic list
/csi_cam_0/camera_info
/csi_cam_0/image_raw
/csi_cam_0/image_raw/compressed
/csi_cam_0/image_raw/compressed/parameter_descriptions
/csi_cam_0/image_raw/compressed/parameter_updates
/csi_cam_0/image_raw/compressedDepth
/csi_cam_0/image_raw/compressedDepth/parameter_descriptions
/csi_cam_0/image_raw/compressedDepth/parameter_updates
/csi_cam_0/image_raw/theora
/csi_cam_0/image_raw/theora/parameter_descriptions
/csi_cam_0/image_raw/theora/parameter_updates
/rosout
/rosout_agg

cs18resch01001@nano-ub18:~$ rostopic hz /csi_cam_0/image_raw
subscribed to [/csi_cam_0/image_raw]
average rate: 20.538
        min: 0.043s max: 0.050s std dev: 0.00139s window: 21
average rate: 20.435
        min: 0.043s max: 0.050s std dev: 0.00101s window: 42
average rate: 20.404
        min: 0.043s max: 0.050s std dev: 0.00085s window: 62
average rate: 20.388
        min: 0.043s max: 0.051s std dev: 0.00078s window: 82
average rate: 20.379
        min: 0.043s max: 0.051s std dev: 0.00070s window: 103
average rate: 20.373
        min: 0.043s max: 0.051s std dev: 0.00064s window: 123
average rate: 20.369
        min: 0.043s max: 0.051s std dev: 0.00062s window: 143
average rate: 20.365
        min: 0.043s max: 0.051s std dev: 0.00058s window: 164
average rate: 20.362
        min: 0.043s max: 0.051s std dev: 0.00056s window: 184
```


