#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

 

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

   print () {
    for (let i = 0; i < this.height; i++) {
      let d = '';
      for (let j = 0; j < this.width; j++) {
        d += 'X';
      }
      console.log(d);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
