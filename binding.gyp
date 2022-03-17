{
    "defines": [
        "NAPI_VERSION=<(napi_build_version)",
    ],
    "targets": [
        {
            "target_name": "canon_api",
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'cflags': ['-flat_namespace'],
            'cflags_cc': ['-flat_namespace'],
            'defines': [ 'NAPI_ENABLE_CPP_EXCEPTIONS' ],
            "sources": [
                "./src/library/api-error.cc",
                "./src/library/api-identifier.cc",
                "./src/library/base64.cc",
                "./src/library/camera.cc",
                "./src/library/camera-browser.cc",
                "./src/library/camera-file.cc",
                "./src/library/camera-property.cc",
                "./src/library/camera-api.cc",
                "./src/library/directory.cc",
                "./src/library/labels.cc",
                "./src/library/object-event.cc",
                "./src/library/option.cc",
                "./src/library/output-device.cc",
                "./src/library/aperture.cc",
                "./src/library/exposure-compensation.cc",
                "./src/library/file-format.cc",
                "./src/library/flag.cc",
                "./src/library/image-quality.cc",
                "./src/library/iso-sensitivity.cc",
                "./src/library/shutter-speed.cc",
                "./src/library/state-event.cc",
                "./src/library/time-zone.cc",
                "./src/library/utility.cc",
                "./src/library/volume.cc",
            ],
            "include_dirs": [
                "./src",
                "<(module_root_dir)/third_party/EDSDK/Header",
                "<!(node -p \"require('node-addon-api').include_dir\")"
            ],
            'link_settings': {
              'ldflags': [
                '-flat_namespace'
              ],
              'libraries': [
                '../third_party/EDSDK/Framework/EDSDK.framework/EDSDK',
              ],
            },
            "copies": [
                {
                    "destination": "<(PRODUCT_DIR)",
                    "files": [
                        "<(module_root_dir)/third_party/EDSDK/Framework/EDSDK.framework",
                    ]
                }
            ],
            "xcode_settings": {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
              "MACOSX_DEPLOYMENT_TARGET": "12.2",
              "CLANG_CXX_LANGUAGE_STANDARD": "c++17"
            },
        }
    ],
}
