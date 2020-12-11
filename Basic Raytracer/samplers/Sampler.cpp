#include "Sampler.hpp"
#include "../cameras/Camera.hpp"
#include "../utilities/Ray.hpp"
#include "../world/ViewPlane.hpp"

Sampler::Sampler()
{
	camera_ptr = NULL;
	viewplane_ptr = NULL;
}

Sampler::Sampler(Camera* c_ptr, ViewPlane* v_ptr)
{
	camera_ptr = c_ptr;
	viewplane_ptr = v_ptr;
}
