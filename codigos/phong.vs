//Vertex Shader
varying vec4 eyePosition;
varying vec3 diffuseColor,specularColor,emissiveColor;
varying vec3 ambientColor,normal; 
varying float shininess;

void main()
{
gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
eyePosition = gl_ModelViewMatrix * gl_Vertex;
normal = gl_NormalMatrix * gl_Normal;
diffuseColor = vec3(gl_FrontMaterial.diffuse);
specularColor = vec3(gl_FrontMaterial.specular);
emissiveColor = vec3(gl_FrontMaterial.emission);
ambientColor = vec3(gl_FrontMaterial.ambient);
shininess = gl_FrontMaterial.shininess;
}