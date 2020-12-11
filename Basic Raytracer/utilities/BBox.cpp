#include "BBox.hpp"
#include "Point3D.hpp"
#include "../geometry/Geometry.hpp"

BBox::BBox(const Point3D& min, const Point3D& max)
{
	pmin = min;
	pmax = max; 
}

std::string BBox::to_string() const
{
	std::string retval = "(";

	retval.append(pmin.to_string() + ", ");
	retval.append(pmax.to_string() + ")");

	return retval;
}

void BBox::extend(Geometry* g)
{
	BBox box = g->getBBox();
	this->extend(box);
}

void BBox::extend(const BBox& b)
{
	if (this->contains(b.pmin) == false)
	{
		this->pmin = b.pmin;
	}

	if (this->contains(b.pmax) == false)
	{
		this->pmax = b.pmax;
	}
}

bool BBox::contains(const Point3D& p)
{
	if (p.x > pmax.x || p.x < pmin.x)
		return false;
	if (p.y > pmax.y || p.y < pmin.y)
		return false;
	if (p.z > pmax.z || p.z < pmin.z)
		return false;

	return true;
}