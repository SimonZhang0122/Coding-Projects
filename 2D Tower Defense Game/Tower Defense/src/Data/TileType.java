package Data;

public enum TileType {// this class creates references for all textures

	Grass("Grass64 texture", true), Dirt("Dirt64 texture", false), Water("Water64 texture", false),
	NULL("Water64 texture", false);// false means you can't build anything on top of this texture type

	String textureName;
	boolean buildable;

	TileType(String textureName, boolean buildable) {
		this.textureName = textureName;
		this.buildable = buildable;
	}
}
