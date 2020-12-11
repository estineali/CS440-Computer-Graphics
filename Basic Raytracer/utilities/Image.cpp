#include "Image.hpp"
#include "RGBColor.hpp"
#include "../world/ViewPlane.hpp"

Image::Image(int hres, int vres)
{
	this->hres = hres;
	this->vres = vres;
}

Image::Image(const ViewPlane& vp)
{
}
