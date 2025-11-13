package ar.edu.unlp.info.oo1.ej10_jobScheduler;

import java.util.List;

public interface Strategy {
    public JobDescription next(List<JobDescription> jobs) ;
    }

