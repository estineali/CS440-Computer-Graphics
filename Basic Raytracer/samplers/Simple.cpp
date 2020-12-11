#include "Simple.hpp"

Simple::Simple(Camera* c_ptr, ViewPlane* v_ptr)
{
	camera_ptr = c_ptr;
	viewplane_ptr = v_ptr;
}

Simple::Simple(const Simple& camera)
{
	camera_ptr = camera.camera_ptr;
	viewplane_ptr = camera.viewplane_ptr;
}

Simple& Simple::operator=(const Simple& other)
{
	camera_ptr = other.camera_ptr;
	viewplane_ptr = other.viewplane_ptr;

	return *this;
}
