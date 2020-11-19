package com.bogotobogo.examples.junitmavenexample;
import static org.junit.Assert.*;

import org.junit.Test;

public class ExampleTest {
 @Test public void t1() {
  Example tester = new Example();
  tester.a(-1);
  tester.a(1);
  tester.b(1);
  assertEquals(9, tester.x()); // failed -> 8
  }

  @Test public void t2() {
  Example tester = new Example();
  tester.a(1);
  tester.b(1);
  assertEquals(4, tester.x()); // failed -> 3
  }
  
  @Test public void t3() {
  Example tester = new Example();
  tester.a(1);
  tester.b(0);
  assertEquals(1, tester.x());
  }
  
  @Test public void t4() {
  Example tester = new Example();
  tester.a(-1);
  tester.a(1);
  tester.b(-1);
  assertEquals(7, tester.x());
  }
}

