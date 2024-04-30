
問個問題
我目前在寫個截圖的函數
長這樣
```python
def screenshot(screen_index: int):
    with mss.mss() as sct:
        sct.shot(mon=(screen_index+1), output="assets\\screenshots\\temp.png")
        screenshot_np = cv2.imread("assets\\screenshots\\temp.png")
        return screenshot_np
```
我會用shot而不是用grab是因為
如果用grab在擷取經過125%縮放的全螢幕時
會以縮放後的長寬(1536*864)來擷取1080p的螢幕
目前問題是
在外部獨立的測試區域測試這個函數時
他是可以正常擷取全螢幕
但把這個函數ctrl c ctrl v到我的專案內時
卻還是發生如grab一樣的問題
想問這個問題能從何解決起