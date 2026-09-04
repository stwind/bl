from string import Template

LIB = """float length2(vector v) {
  vector a = abs(v);
  float m = max(a.x, a.y);
  vector am = a / m;
  return select(0, hypot(am.x, am.y) * m, m > 0);
}
float fract(float x) { return x - floor(x); }
float logn(float x, float b) { return log(x) / log(b); }
float norm(float x, float a, float b) { return (x - a) / (b - a); }
float satnorm(float x, float a,float b) { return clamp(norm(x,a,b), 0.0, 1.0); }
float aastep0(float x, float w) { return satnorm(x, w - .5, w + .5); }
float triangle(float x) { return .5 - abs(fract(x) - .5); }

float contour(float v, float g, float w, float f) {
  return 1 - aastep0(triangle(v * f) / (2 * g * f), w);
}
float contour_adaptive(float v, float g, float w, float f, float b, float m) {
  float s = select(0, -logn(m * g, b), g > 1e-6);
  float fy = f * pow(b, floor(s));
  float vfy = v * fy, gfy = g * fy;
  float c0 = 1 - aastep0(triangle(vfy) / gfy, w);
  float c1 = 1 - aastep0(triangle(vfy / b) / (gfy / b), w);
  float c2 = 1 - aastep0(triangle(vfy * b) / (gfy * b), w);
  float t = (pow(b, fract(s)) - 1.) / (b - 1.);
  return (mix(c1, c2, t) + c0) * .5;
}

vector bary() { return vector(1 - u - v, u, v); }
"""


def shader(text):
    return Template(f"$LIB {text}").substitute(LIB=LIB)
