from __future__ import annotations


def image_matching_status() -> dict[str, str]:
    return {
        "stage": "C",
        "status": "not_enabled",
        "reason": "No item images are present in the Stage A dataset.",
        "recommendation": (
            "When images are available, evaluate a pretrained CLIP-style model as supporting evidence only. "
            "Do not use visual similarity alone as proof of ownership."
        ),
    }

