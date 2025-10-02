import { Component, inject, OnInit } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-register-end',
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './register-end.component.html',
})
export class RegisterEndComponent implements OnInit {
  private apiService = inject(ApiService);

  registerForm!: FormGroup;
  isLoading: boolean = false;

  constructor(private fb: FormBuilder) {}

  ngOnInit() {
    this.registerForm = this.fb.group({
      placa: ['', [Validators.required]],
      hora_salida: ['', [Validators.required]],
    });
  }

  onSubmit() {
    if (this.registerForm.valid) {
      this.isLoading = true;
      const formData = this.registerForm.value;
      const placa = formData.placa;
      const horaSalidaISO = new Date(formData.hora_salida).toISOString();

      //Obtener el último registro activo
      this.apiService.getLastRegister(placa).subscribe({
        next: (res) => {
          //si tiene id, es porque existe un registro activo
          if (res.id) {
            //actualizar el registro activo con la hora de salida
            this.apiService.setRegister(res.id, { hora_salida: horaSalidaISO }).subscribe({
              next: (res) => {
                console.log(res);
              },
            });
          }
        },
      });
    }
  }
}
