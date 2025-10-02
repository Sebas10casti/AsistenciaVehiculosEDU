import { Component, inject, OnInit } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-register-start',
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './register-start.component.html',
})
export class RegisterStartComponent implements OnInit {
  private apiService = inject(ApiService);

  registerForm!: FormGroup;
  isLoading: boolean = false;

  constructor(private fb: FormBuilder) {}

  ngOnInit() {
    this.registerForm = this.fb.group({
      placa: ['', [Validators.required]]
    });
  }

  onSubmit() {
    if (this.registerForm.valid) {
      this.isLoading = true;
      const placa = this.registerForm.get('placa')?.value;
      this.apiService.createRegister({ placa}).subscribe({
        next: (res) => {
          console.log(res);
        }
      })
    }
  }
}
