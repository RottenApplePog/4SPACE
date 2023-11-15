#version 330 core

uniform sampler2D tex;

in vec2 uvs;

out vec4 f_color;


void main() {
    if(texture(tex, uvs).r == 0.0f && texture(tex, uvs).g == 0.0f && texture(tex, uvs).b == 0.0f)
    {
        discard;
    }
    f_color = texture(tex, uvs);
}


/*
void main() {
    f_color = vec4(texture(tex, uvs).rgb, 1.0);

}
*/
