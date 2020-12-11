#include "RGBColor.hpp"
#include <cstdint>


RGBColor::RGBColor()
{
	r = g = b = 0;
}

RGBColor::RGBColor(float c)
{
	if (c > 1)
		r = g = b = 1;
	else if (c < 0)
		r = g = b = 0;
	else
		r = g = b = c;
}

RGBColor::RGBColor(float _r, float _g, float _b)
{
	if (_r > 1)
		r = 1;
	else if (_r < 0)
		r = 0;
	else
		r = _r;
	
	if (_g > 1)
		g = 1;
	else if (_g < 0)
		g = 0;
	else
		g = _g;
	
	if (_b > 1)
		b = 1;
	else if (_b < 0)
		b = 0;
	else
		b = _b;

}

//String representation
std::string RGBColor::to_string() const
{
	std::string retval = "(";

	retval.append(std::to_string(r) + ", ");
	retval.append(std::to_string(g) + ", ");
	retval.append(std::to_string(b) + ")");

	return retval;
}

//Arithmetic Operations
RGBColor RGBColor::operator+(const RGBColor& c) const
{
	float new_r = r + c.r;
	new_r = new_r > 1 ? 1 : new_r;
	
	float new_g = g + c.g;
	new_g = new_g > 1 ? 1 : new_g;
	
	float new_b = b + c.b;
	new_b = new_b > 1 ? 1 : new_b;

	return RGBColor(new_r, new_g, new_b);
}

RGBColor& RGBColor::operator+=(const RGBColor& c)
{
	float new_r = r + c.r;
	r = new_r > 1 ? 1 : new_r;

	float new_g = g + c.g;
	g = new_g > 1 ? 1 : new_g;

	float new_b = b + c.b;
	b = new_b > 1 ? 1 : new_b;

	return *this;
}

RGBColor RGBColor::operator*(const float a) const
{
	float new_r = r*a;
	new_r = new_r > 1 ? 1 : new_r < 0 ? 0 : new_r;

	float new_g = g*a;
	new_g = new_g > 1 ? 1 : new_g < 0 ? 0 : new_g;

	float new_b = b*a;
	new_b = new_b > 1 ? 1 : new_b < 0 ? 0 : new_b;

	return RGBColor(new_r, new_g, new_b);
}

RGBColor& RGBColor::operator*=(const float a)
{
	float new_r = r * a;
	r = new_r > 1 ? 1 : new_r < 0 ? 0 : new_r;

	float new_g = g * a;
	g = new_g > 1 ? 1 : new_g < 0 ? 0 : new_g;

	float new_b = b * a;
	b = new_b > 1 ? 1 : new_b < 0 ? 0 : new_b;

	return *this;
}

RGBColor RGBColor::operator/(const float a) const
{

	float new_r = r / a;
	new_r = new_r > 1 ? 1 : new_r < 0 ? 0 : new_r;

	float new_g = g / a;
	new_g = new_g > 1 ? 1 : new_g < 0 ? 0 : new_g;

	float new_b = b / a;
	new_b = new_b > 1 ? 1 : new_b < 0 ? 0 : new_b;

	return RGBColor(new_r, new_g, new_b);
}

RGBColor& RGBColor::operator/=(const float a)
{
	float new_r = r / a;
	r = new_r > 1 ? 1 : new_r < 0 ? 0 : new_r;

	float new_g = g / a;
	g = new_g > 1 ? 1 : new_g < 0 ? 0 : new_g;

	float new_b = b / a;
	b = new_b > 1 ? 1 : new_b < 0 ? 0 : new_b;

	return *this;
}

RGBColor RGBColor::operator*(const RGBColor& c) const
{
	float new_r = r * c.r;
	new_r = new_r > 1 ? 1 : new_r < 0 ? 0 : new_r;

	float new_g = g * c.g;
	new_g = new_g > 1 ? 1 : new_g < 0 ? 0 : new_g;

	float new_b = b * c.b;
	new_b = new_b > 1 ? 1 : new_b < 0 ? 0 : new_b;

	return RGBColor(new_r, new_g, new_b);
}

bool RGBColor::operator==(const RGBColor& c) const
{
	return (r == c.r && g == c.g && b == c.b);
}

RGBColor RGBColor::powc(float p) const
{
	float new_r = pow(r, p);
	new_r = new_r > 1 ? 1 : new_r < 0 ? 0 : new_r;

	float new_g = pow(g, p);
	new_g = new_g > 1 ? 1 : new_g < 0 ? 0 : new_g;

	float new_b = pow(b, p);
	new_b = new_b > 1 ? 1 : new_b < 0 ? 0 : new_b;

	return RGBColor(new_r, new_g, new_b);
}

float RGBColor::average() const
{
	return (r + g + b)/3;
}

//Multiplication by a float 
RGBColor operator*(const float a, const RGBColor& c)
{
	return c * a;
}
