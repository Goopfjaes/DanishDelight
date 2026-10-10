package dk.danskdelight.registry;

import dk.danskdelight.DanskDelight;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;

public class ModCreativeTabs {
    public static final DeferredRegister<CreativeModeTab> TABS =
            DeferredRegister.create(Registries.CREATIVE_MODE_TAB, DanskDelight.MOD_ID);

    public static final RegistryObject<CreativeModeTab> DANSK_DELIGHT = TABS.register("danskdelight",
            () -> CreativeModeTab.builder()
                    .title(Component.translatable("itemGroup." + DanskDelight.MOD_ID))
                    .icon(() -> new ItemStack(ModItems.FLAESKEFRADER.get()))
                    .displayItems((parameters, output) -> {
                        output.accept(ModItems.KULOR.get());
                        output.accept(ModItems.BRUN_SOVS.get());
                        output.accept(ModItems.BERNAISE.get());
                        output.accept(ModItems.FLAESKESTEG.get());
                        output.accept(ModItems.FLAESKEFRADER.get());
                        output.accept(ModItems.KYLLING_BERNAISE.get());
                    })
                    .build());
}
