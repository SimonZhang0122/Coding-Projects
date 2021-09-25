package Data;

public interface Entity {// lists of variables for different type of cannon towers

	public float getX();

	public float getY();

	public int getWidth();

	public int getHeight();

	public void setX(float x);

	public void setY(float y);

	public void setWidth(int width);

	public void setHeight(int height);

	public void update();

	public void draw();
}
