#include "Cosine.hpp"

Cosine::Cosine()
{
	color = RGBColor();
}

Cosine::Cosine(float c)
{
	color = RGBColor(c);
}

Cosine::Cosine(float r, float g, float b)
{
	color = RGBColor(r, g, b);
}

Cosine::Cosine(const RGBColor& c)
{
	color = c;
}

Cosine::Cosine(const Cosine& other)
{
	color = other.color;
}

Cosine& Cosine::operator=(const Cosine& other)
{
	color = other.color;

	return *this;
}




