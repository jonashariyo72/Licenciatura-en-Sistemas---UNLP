package ar.edu.unlp.info.oo1.ej10_jobScheduler;

import java.util.ArrayList;
import java.util.List;

public class JobScheduler  {
    protected List<JobDescription> jobs;
    private Strategy estrategia;
    
    
    public JobScheduler () {
        this.jobs = new ArrayList<>();
        this.estrategia = new StrategyFIFO ();
    }

    public void schedule(JobDescription job) {
        this.jobs.add(job);
    }

    public void unschedule(JobDescription job) {
        if (job != null) {
            this.jobs.remove(job);
        }
    }

    public Strategy getStrategy() {
        return this.estrategia; 
    }

    public List<JobDescription> getJobs(){
        return jobs;
    }

    public void setStrategy(Strategy unaEstrategia) {
        this.estrategia = unaEstrategia;
    }
    
     public JobDescription next() {
    	 	
    	 JobDescription nextJob = estrategia.next(this.jobs);
           this.unschedule(nextJob);
             return nextJob; 
     }
    
     
    
    //public JobDescription next() {
      //  JobDescription nextJob = null;

       // switch (strategy) {
         //   case "FIFO":
           //     nextJob = jobs.get(0);
             //   this.unschedule(nextJob);
              //  return nextJob; 

            //case "LIFO":
             //   nextJob = jobs.get(jobs.size()-1);
              //  this.unschedule(nextJob);
               // return nextJob;

            // case "HighestPriority":
              //  nextJob = jobs.stream()
               //     .max((j1,j2) -> Double.compare(j1.getPriority(), j2.getPriority()))
                //    .orElse(null);
              //  this.unschedule(nextJob);
              //  return nextJob;

          //  case "MostEffort":
             //   nextJob = jobs.stream()
              //      .max((j1,j2) -> Double.compare(j1.getEffort(), j2.getEffort()))
              //      .orElse(null);
          //      this.unschedule(nextJob);
              //  return nextJob;
      //  }
       // return null;
   // }

}
