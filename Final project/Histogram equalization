//Librerias que vamos a utilizar 
#include <stdio.h>
#include<stdlib.h>
#include<omp.h>
#include<math.h>
//Stn master nos ayudará a manejar las imagenes 
#define STB_IMAGE_IMPLEMENTATION
#include "stb-master/stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb-master/stb_image_write.h"
//Caracteristicas  de una imagen 
#define COLOR_VALUE 256
#define QUALITY 100 
//Prototipo de funciones 

double equilizeImage_secuencial(unsigned char *srcIma);
//void equilizeImage_paralell(unsigned char *srcIma);

unsigned char *empty_array_UC(long size);
long *empty_array_LONG(long size);

long min_cdf_SEQUENTIAL(long *cdf);
//----------------SECUENCIAL---------------// 

long *histogram_space(unsigned char *image, long size, int channels);
long *cumulative_distribution_function_SEQUENTIAL(long *histogram);
long *equalized_value_distribution_SEQUENTIAL(long *cummulative_value, long min, long  size);
unsigned char *equalized_Image(unsigned char  *first_Image, int channels, long *equalized_value, long size);
 //csv
void csv(char *image_name, long *histogram, long *equalized_histogram, char *suffix);
char *create_new_file(char *image_source, char *suffix);
char *file_name(char *image_source);

int main(int argc, char *argv[]){
    if(argc < 2){
        printf("Using wrong size of a image");
        return -1;
    }

    char *image_source = argv[1];
    int width, height, channels; 
    unsigned char *image = stbi_load(image_source, &width, &height, &channels, 0);
    double tIni, tSecuencia, tParalelo, tFinal; 

    if(image = NULL){
        printf("There is no image");
        return -1; 
    }
    
    //de aqui para adelante es secuencial 

    

    return 0; 


}

//Creamos arreglos tipo UC y LONG para poder trabajar con la informacion 
unsigned char *empty_array_UC(long size){
    unsigned char *new_array_UC = malloc(sizeof(unsigned char) * size);
    for(int i = 0; i < size; i++ ){
        new_array_UC[i] = 0;
    }
    return new_array_UC; 
}

long *empty_array_LONG(long size){
    long *new_array_LONG = malloc(sizeof(long) * size);
    for(int i = 0; i < size; i++ ){
        new_array_LONG[i] = 0;
    }
    return new_array_LONG; 
}
 
//----------SECUENCIALL------------
long *histogram_space(unsigned char *image, long size, int channels){
    long *new_histogram = empty_array_LONG(COLOR_VALUE); 
    for(int i = 0; i < size * channels; i=i+channels){
        new_histogram[(int)image[i]]; //Aqui decimos que el valor del pixel en la imagen será el valor asignado en el new histogram
    }
    return new_histogram; 
}

long *cumulative_distribution_function_SEQUENTIAL(long *histogram){
    long *cdf = empty_array_LONG(COLOR_VALUE);
    for(int i = 1; i< COLOR_VALUE; i++){
        cdf[i] = histogram[i-1] + cdf[i]; //sumas los valores 
    }
    return  cdf; 
}

long min_cdf_SEQUENTIAL(long *cdf){
    long min = cdf[0]; 
    for(int i = 0; i < COLOR_VALUE; i++){
        if(min > cdf[i]){
            min = cdf[i];
        }
    }
    return min; 
}

long *equalized_value_distribution_SEQUENTIAL(long *cummulative_value, long min, long  size){
    long *equilizeImage_value = empty_array_LONG(COLOR_VALUE);
    double factor = ((double) COLOR_VALUE - 2) / ((double) size - min); 
    for(int i=0; i<COLOR_VALUE; i++){
        equilizeImage_value[i] = round( ((double)(cummulative_value[i] - min) * factor) + 1); //SI esto no funciona separarlo en una variable
    }
    return equilizeImage_value; 
}

unsigned char *equalized_Image(unsigned char  *first_Image, int channels, long *equalized_value, long size){
    unsigned char *second_Image = empty_array_UC(size* channels); 
    for(int i = 0; i < size*channels; i ++){
        unsigned char original_image_value = first_Image[i]; 
        if(i % channels == 0){
            second_Image[i] = (unsigned char) equalized_value[original_image_value];
        }else{
            second_Image[i] = (unsigned char) original_image_value;
        }
        return second_Image; 
    }
}

double final_sequential_equalization(unsigned char *image, int width, int height, int channels, char *name_of_image){
    
    double t1 = omp_get_wtime();

    long size = height * width; 
    long *image_histogram = histogram_space(image, size, channels);
    long *cdf  = cumulative_distribution_function_SEQUENTIAL(image_histogram); //
    long minimun_cdf = min_cdf_SEQUENTIAL(cdf);
    long *cumulative_distribution = equalized_value_distribution_SEQUENTIAL(cdf, minimun_cdf, size);
    unsigned char *equalizedImage = equalized_Image(image, channels, cumulative_distribution, size);
    long *equalized_histogram = histogram_space(equalizedImage, size, channels);

    double t2 = omp_get_wtime();

    csv(); 
    char *first_file_name = file_name(image_source); 
    char *new_file = create_new_file(first_file_name, "_eq_sequential.jpg");
    stbi_write_jpg(new_file, width, height, channels, equalizedImage, QUALITY);
    csv(new_histogram, equalized_histogram, "sequential");

    stbi_image_free(image);
    stbi_image_free(equalizedImage);

    free(new_histogram);
    free(cdf);
    free(cumulative_distribution);
    free(equalizedImage);
    free(first_file_name);
    free(new_file);
}
//OBTENEMOS PARA CVF

void csv(char *image_name, long *histogram, long *equalized_histogram, char *suffix){
    //Creamos el archivo
    char *name_of_image = create_new_file("out/", image_name); 
    name_of_image = create_new_file(name_of_image, "_histogram");
    name_of_image = create_new_file(name_of_image, suffix); 
    name_of_image = create_new_file(name_of_image, ".csv"); 
    FILE *csv_file = fopen(name_of_image, "w+");

    for(int i = 0; i < COLOR_VALUE; i++){
        fprintf(csv_file, "%d, %ld,  %ld\n", i, histogram[i], equalized_histogram[i]);
    }
    fclose(csv_file); 
}


char *file_name(char *image_source){
    //ontenemos el nombre de la imagen
    char *name_of_image = strrchr(image_source, '/'); //bussca la ultima ocurrencia
    if(name_of_image == NULL){
        name_of_image = image_source; 
    } else{
        name_of_image ++; 
    }
    return strtok(name_of_image, ".");  //Rinoe la cadena 
}

char *create_new_file(char *image_source, char *suffix){
    char *new_file = malloc(sizeof(char)*1000);
    snprintf(new_file, sizeof(char)*1000, "%s%s", image_source, suffix);//print the output as a buffer
    return new_file; 
}
