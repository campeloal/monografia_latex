uniform sampler2D colormap;
varying vec2  TexCoord;

void main(void) {
	gl_FragColor = texture2D(colormap, TexCoord);
}