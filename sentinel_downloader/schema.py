CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "debug": {"type": "boolean"},
        "instance_id": {"type": "string"},
        "layer": {"type": "string"},
        "times": {"type": "array"},
        "bounding_box": {"type": "array"},
        "width": {"type": "integer"},
        "height": {"type": "integer"},
        "max_cloud_percentage": {"type": "number"},
        "images_dir": {"type": "string"},
    },
    "required": [
        "instance_id",
        "layer",
        "times",
        "bounding_box",
        "width",
        "height",
        "images_dir",
    ],
}
