// typedef struct {int rank, size; } MPI_Comm;
// typedef struct ompi_communicator_t *MPI_Comm;
// extern MPI_Comm MPI_COMM_WORLD;


// void nek_init_(MPI_Comm comm);
void nek_init_(int* comm);
void nek_solve_();
void nek_end_();
