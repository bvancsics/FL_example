package com.bogotobogo.examples.junitmavenexample;
import java.lang.Math;

public class Example{
  private int _x = 0;
  private int _s = 0;
  public int x() {return _x;}

  public void a(int i){
    _s = 0;
    if (i==0) return;
    if (i<0)
      for (int y=0;y<=4;y++)
        f(i);
    else
      g(i);
  }
  
  public void b(int i){
    _s = 1;
    if (i==0) return;
    if (i<0)
      a(Math.abs(i));
    else
      for (int y=0;y<=1;y++)
        g(i);
  }

  private void f(int i){
    _x -= i;
  }

  private void g(int i){
    _x += (i+_s); //should be _x += i;
  }
}