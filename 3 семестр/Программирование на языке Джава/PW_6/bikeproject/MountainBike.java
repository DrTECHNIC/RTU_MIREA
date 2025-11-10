package bikeproject;

public class MountainBike extends Bike implements MountainParts
{
	private String suspension, type;
	private int frameSize;

	public MountainBike()
	{ this("Bull Horn", "Hardtail", "Maxxis", "dropper", 27, "RockShox XC32", "Pro", 19); }

	public MountainBike(String handleBars, String frame, String tyres, String seatType, int numGears,
						String suspension, String type, int frameSize)
	{
		super(handleBars, frame, tyres, seatType, numGears);
		this.suspension = suspension;
		this.type = type;
		this.frameSize = frameSize;
	}

	public String getSuspension() { return this.suspension; }

	public void setSuspension(String newValue) { this.suspension = newValue; }

	public String getType() { return this.type; }

	public void setType(String newValue) { this.type = newValue; }

	public void printDescription()
	{
		super.printDescription();
		System.out.println("This mountain bike is a " + this.type + " bike and has a " + this.suspension
				+ " suspension and a frame size of " + this.frameSize + " inches.");
	}
}
