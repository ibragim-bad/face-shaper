import EXIF from 'exif-js'

export default function(file, setRotate) {

  EXIF.getData(file, function () {
    var orientation = EXIF.getTag(this, "Orientation");
    let rotatePic = 0;
    switch (orientation) {
      case 8:
        rotatePic = 270;
        break;
      case 6:
        rotatePic = 90;
        break;
      case 3:
        rotatePic = 180;
        break;
      default:
        rotatePic = 0;

    }
    setRotate(rotatePic);
  });

}