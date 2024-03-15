if __name__ == "__main__":
    import cv2 
    from codeformer.app import inference_app

    img = cv2.imread("test.png")
    img = inference_app(
      image=img,
      background_enhance=True,
      face_upsample=True,
      upscale=2,
      codeformer_fidelity=0.5,
       min_size= 50, 
       max_size= 150
    )
    cv2.imwrite("out.png", img)