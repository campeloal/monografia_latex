//Fragment shader
varying vec4 eyePosition;
varying vec3 normal,diffuseColor,specularColor;
varying vec3 emissiveColor,ambientColor;
varying float shininess;
void main()
{
 const vec3 lightColor = vec3(1, 1, 1);
 const vec3 globalAmbient = vec3(0.2, 0.2, 0.2);
 vec3 P = vec3(eyePosition);
 vec3 N = normalize(normal);
 vec3 emissive = emissiveColor;
 vec3 ambient = ambientColor * globalAmbient;
 vec3 L = normalize(vec3(gl_LightSource[0].position) - P);
 float diffuseLight = max(dot(N, L), 0);
 vec3 diffuse = diffuseColor * lightColor * diffuseLight;
// Compute the specular term
 vec3 V = normalize(-P);
 vec3 H = normalize(L + V);
 float specularLight = pow(max(dot(N, H),0), shininess);
 if(diffuseLight <= 0) specularLight = 0;
 vec3 specular = specularColor * lightColor * specularLight;
 gl_FragColor.xyz = emissive + ambient + diffuse + specular;
 gl_FragColor.w = 1.0;
}