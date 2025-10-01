import { Component, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-create-vehicle',
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './create-vehicle.component.html',
})
export class CreateVehicleComponent {
  private fb = inject(FormBuilder);
  private router = inject(Router);
  private apiService = inject(ApiService);
  
  vehicleForm: FormGroup;
  isSubmitting = false;

  constructor() {
    this.vehicleForm = this.fb.group({
      tipo: ['', Validators.required],
      nombre_dueno: ['', [Validators.required, Validators.maxLength(150)]],
      documento: ['', [Validators.required, Validators.maxLength(50)]],
      placa: ['', Validators.maxLength(30)],
      serial: ['', Validators.maxLength(80)],
      color: ['', [Validators.required, Validators.maxLength(50)]],
      marca: ['', Validators.maxLength(80)],
      area: ['', Validators.required]
    });
  }

  onSubmit() {
    if (this.vehicleForm.valid) {
      this.isSubmitting = true;
      const formData = this.vehicleForm.value;
      
      this.apiService.createVehicle(formData).subscribe({
        next: (response) => {
          console.log('Vehículo creado:', response);
          this.router.navigate(['']);
        },
        error: (error) => {
          console.error('Error al crear vehículo:', error);
          this.isSubmitting = false;
        }
      });
    }
  }

  onCancel() {
    this.router.navigate(['/vehicles']);
  }
}
