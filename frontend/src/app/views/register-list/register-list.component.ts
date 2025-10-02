import { Component, effect, inject } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { rxResource } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-register-list',
  imports: [],
  templateUrl: './register-list.component.html',
})
export class RegisterListComponent {
  private apiService = inject(ApiService);

  public registersResource = rxResource({
    stream: () => this.apiService.getRegisters(),
    defaultValue: [],
  });

  public registersResourceEffect = effect(() => {
    console.log(this.registersResource.value());
  });
}
