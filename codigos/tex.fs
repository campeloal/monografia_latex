uniform sampler2D myTexture;
varying vec2 TexCoord;

void main (void)
{
  gl_FragColor  = texture2D(myTexture, TexCoord);         
}