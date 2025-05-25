#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define EPS       0.001    
#define K         2        
#define DEFFAULT_ITER  400 
#define MAX_LINE  1024     


static void validate_clusters(int k, int n) {
    if (k <= 1 || k >= n) {
        fprintf(stderr, "Error: incorrect number of clusters (K=%d, N=%d)\n", k, n);
        exit(EXIT_FAILURE);
    }
}

static void validate_iter(int iter) {
    if (iter <= 1 || iter >= 1000) {
        fprintf(stderr, "Error: incorrect max iterations (%d)\n", iter);
        exit(EXIT_FAILURE);
    }
}
double distance(const double *x1, const double *x2, int m) {
	double d, r = 0.0;
	while (m--) {
		d = *(x1++) - *(x2++);
		r += d * d;
	}
	return r;
}


/*
int main(int argc, char *argv[]) 
{
    //init parameters from command line - need  to be added
    iter = DEFFAULT_ITER;
    K = 2;
    
    validate_iter(iter);
    validate_clusters(K, n);
}
*/

#include <stdio.h>
#include <stdlib.h>

struct cord
{
    double value;
    struct cord *next;
};
struct vector
{
    struct vector *next;
    struct cord *cords;
};
/**
 * Frees all the cords in a single vector,
 * then frees the vector itself.
 */
 /*void free_vectors(struct vector *head_vec) {
    struct vector *v = head_vec;
    while (v) {
         first free the coordinate‐list 
        struct cord *c = v->cords;
        while (c) {
            struct cord *next_c = c->next;
            free(c);
            c = next_c;
        }

         then free this vector node and advance 
        struct vector *next_v = v->next;
        free(v);
        v = next_v;
    }
}
*/

int main(int argc, char **argv)
{

    struct vector *head_vec, *curr_vec, *next_vec;
    struct cord *head_cord, *curr_cord, *next_cord;
    int i, j, rows = 0, cols;
    double n;
    char c;

    /*int K      = (int)strtol(argv[1], NULL, 10);
    int iter   = (int)strtol(argv[2], NULL, 10);

    //printf("K = %d\n", K);
    //printf("iter = %d\n", iter);
    */
    head_cord = malloc(sizeof(struct cord));
    curr_cord = head_cord;
    curr_cord->next = NULL;

    head_vec = malloc(sizeof(struct vector));
    curr_vec = head_vec;
    curr_vec->next = NULL;
    

    while (scanf("%lf%c", &n, &c) == 2)
    {

        if (c == '\n')
        {
            curr_cord->value = n;
            curr_vec->cords = head_cord;
            curr_vec->next = malloc(sizeof(struct vector));
            curr_vec = curr_vec->next;
            curr_vec->next = NULL;
            head_cord = malloc(sizeof(struct cord));
            curr_cord = head_cord;
            curr_cord->next = NULL;
            continue;
        }

        curr_cord->value = n;
        curr_cord->next = malloc(sizeof(struct cord));
        curr_cord = curr_cord->next;
        curr_cord->next = NULL;
    }

    
    /* free memory

    free_vectors(head_vec);*/

    return 0;
}
