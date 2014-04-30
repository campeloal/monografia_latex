// red.vs
//just multiplies vertex position vector 
// by the modelview and projection matrices.

uniform float time;

void main()
{	

   gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;

}

