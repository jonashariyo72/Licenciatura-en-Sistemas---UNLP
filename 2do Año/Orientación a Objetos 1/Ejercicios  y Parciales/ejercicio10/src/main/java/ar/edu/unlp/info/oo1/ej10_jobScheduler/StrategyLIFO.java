package ar.edu.unlp.info.oo1.ej10_jobScheduler;

import java.util.List;

public class StrategyLIFO implements Strategy {
	public JobDescription next(List<JobDescription> jobs) {
		return jobs.get(jobs.size()-1);
		
	}
}
